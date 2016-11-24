/**
 * Created by Artem on 12/4/2016.
 */

var addBoards = function() {
    var $start_pos = $('#id_start_pos');
    $start_pos.after('<div id="board" style="width: 400px"></div>');
    $('#board').after('<input class="btn btn-primary" type="button" id="startBtn" value="Start" />');
    var $startBtn = $('#startBtn');
    $startBtn.after('<input class="btn btn-primary" type="button" id="clearBtn" value="Clear" />');
    $start_pos.val('');
    var board = ChessBoard('board', {
      draggable: true,
      dropOffBoard: 'trash',
      sparePieces: true,
        onChange: function() {
            console.log('drop');
            console.log(board.position());
            $start_pos.val(board.fen())
        }
    });

    $startBtn.on('click', board.start);
    $('#clearBtn').on('click', board.clear);
//--- end example JS ---

};

$(document).ready(addBoards);