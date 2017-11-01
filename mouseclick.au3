;Script for mouse movement every 5 seconds
;This will help you not to lock PC in idle state
;MouseGetPos function will return mouse co-ordinates x and y
;MouseMove function will move the mouse based on co-ordinate arguments


While 1
    Sleep( 5000 )
    $CurPos = MouseGetPos ( )
	;ConsoleWrite("before - "& $CurPos[0])
	MouseMove ( $CurPos[0] + 1, $CurPos[1] )
    MouseMove ( $CurPos[0] - 1, $CurPos[1] )
WEnd