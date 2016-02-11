*** Settings ***
Library  WebSocketClient

*** Test Cases ***
Echo
    ${my_websocket}=  WebSocketClient.Connect  ws://echo.websocket.org
    WebSocketClient.Send  ${my_websocket}  Hello
    ${result}=  WebSocketClient.Recv  ${my_websocket}
    Should Be Equal  Hello  ${result}
    WebSocketClient.Close  ${my_websocket}
