/**
 * Created by Artem on 12/4/2016.
 */

var addBoards = function() {
    var $start_pos = $('#id_start_pos');
    $start_pos.after('<div id="board" style="width: 400px"></div>');
    $start_pos.after('<div id="error_block" class="error text-danger"></div>')
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


        $start_pos.on('input', function (e) {
        var $error_selector = $('#error_block')
        var $create_button_selector = $('#id_create_btn')
        var chess = new Chess();
        fen_state = chess.validate_fen(e.target.value + ' w KQkq - 0 1')
        if( fen_state['valid']) {
            board.position(e.target.value);
            $error_selector.text('');
            $create_button_selector.removeAttr('disabled')
        }
        else {
            $error_selector.text(fen_state['error'])
            $create_button_selector.attr('disabled', 'disabled')
        }

    })

};

$(document).ready(addBoards);