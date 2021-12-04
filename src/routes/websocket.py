from starlette.endpoints import WebSocketEndpoint
from starlette.websockets import WebSocket, WebSocketState
import json
from src.utils.transactions import get_all_transactions
from src.database.models.account import Account


class ClientWebsocketEndpoint(WebSocketEndpoint):
    encoding = "text"
    user_socket_map = {}
    
    async def on_connect(self, websocket: WebSocket):
        await websocket.accept()
        user_id = websocket.query_params['user_id']
        self.user_socket_map[user_id] = websocket
        
        transactions = await get_all_transactions(user_id)
        account = await Account.get_by_user_id(user_id)
        websocket_response = {
            "user_id": user_id,
            "transactions": transactions,
            "balance": float(account.balance)
        }
        await websocket.send_json(websocket_response)
        
        
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