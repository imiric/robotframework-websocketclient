*** Settings ***
Library  WebSocketClient

*** Test Cases ***
Echo
	WebSocketClient.Connect  ws://echo.websocket.org
	WebSocketClient.Send  Hello
	${result}=  WebSocketClient.Recv
	Should Be Equal  Hello  ${result}
	WebSocketClient.Close
