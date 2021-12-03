from starlette.endpoints import WebSocketEndpoint
from starlette.websockets import WebSocket, WebSocketState
import json


class ClientWebsocketEndpoint(WebSocketEndpoint):
    encoding = "text"
    user_socket_map = {}
    
    async def on_connect(self, websocket: WebSocket):
        await websocket.accept()
        user_id = websocket.query_params['user_id']
        self.user_socket_map[user_id] = websocket

    async def on_receive(self, websocket: WebSocket, data):
        user_id = json.loads(data).get('user_id')
        websocket = self.user_socket_map.get(user_id)
        
        if websocket and websocket.client_state == WebSocketState.CONNECTED:
            await websocket.send_json({f'{user_id}': 'Hello from the server!'})
        else:
            await websocket.send_json({'Error': 'Websocket is already closed'})
            
        print(self.user_socket_map)

    async def on_disconnect(self, websocket: WebSocket, close_code):
        pass