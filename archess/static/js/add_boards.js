/**
 * Created by Artem on 12/4/2016.
 */

var addBoards = function() {

    $('#id_start_pos').after('<div id="board" style="width: 400px"></div>');
    $('#board').after('<input class="btn btn-primary" type="button" id="startBtn" value="Start" />');
    $('#startBtn').after('<input class="btn btn-primary" type="button" id="clearBtn" value="Clear" />');

    var board = ChessBoard('board', {
      draggable: true,
      dropOffBoard: 'trash',
      sparePieces: true
    });

    $('#startBtn').on('click', board.start);
    $('#clearBtn').on('click', board.clear);
//--- end example JS ---

};

$(document).ready(addBoards);