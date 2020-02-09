import socketIo from 'socket.io-client';
import { Observable } from 'rxjs';

let SERVER_URL = 'http://localhost:5000';

export class SocketService {
    private socket!: SocketIOClient.Socket;

    public constructor(name: string) {
        SERVER_URL = window.location.hostname + ":5000"
        this.socket = socketIo(SERVER_URL)
        
        this.send("assign_name", name);
        
    }

    public kill() {
        this.socket.disconnect();
    }

    public sendWithoutMessage(type: string): void {
        this.socket.emit(type);
    }

    public send(type: string, message: any): void {
        this.socket.emit(type, message);
    }

    public onEvent(event: string): Observable<any> {
        return new Observable<any>(observer => {
            this.socket.on(event, (data: any) => observer.next(data));
        });
    }
}

export default class StemServer {
    private static socketService: SocketService;

    public static init(name: string): void {
        StemServer.socketService = new SocketService(name);
    }

    public static get(): SocketService {
        return StemServer.socketService
    }
}