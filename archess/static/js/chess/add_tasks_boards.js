/**
 * Created by Artem on 12/5/2016.
 */

$(document).ready(function() {
    boards = document.getElementsByClassName("chessboard");
    console.log(boards.length)
    for (var i = 0; i < boards.length; i++) {
        console.log(stringify(boards[i].id))
            var board = ChessBoard(stringify(boards[i].id), {
                draggable: false,
                });
    }
})