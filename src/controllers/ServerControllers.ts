import socketIo from 'socket.io-client';
import { Observable } from 'rxjs';

const SERVER_URL = 'http://localhost:5000';

export class SocketService {
    private socket!: SocketIOClient.Socket;

    public android_pos: number = -1;
    public cyborg_pos: number = -1;

    private role: string = "";
    private _loaded: boolean = false;

    public constructor() {
        this.socket = socketIo(SERVER_URL);
    }

    public getRole(): string {
        return this.role;
    }

    public loaded(): boolean {
        return this._loaded;
    }

    public kill() {
        this.socket.disconnect();
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
    private static socketService: SocketService = new SocketService();

    public static get(): SocketService {
        return StemServer.socketService
    }
}