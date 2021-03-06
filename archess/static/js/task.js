
var init_play_with_computer = function() {
    var fen_str = $('#start_pos').attr('myattr')

var board,
  game = new Chess(fen_str + ' w KQkq - 0 1');

var onDragStart = function(source, piece, position, orientation) {
  if (game.in_checkmate() === true || game.in_draw() === true ||
    piece.search(/^b/) !== -1) {
    return false;
  }
};

var makeRandomMove = function() {
  var possibleMoves = game.moves();

  if (possibleMoves.length === 0) {
    if(game.in_checkmate()) {
      alert('Congratulations you solved this task')
    }
    else if(game.in_draw()) {
      alert('Game ended in a draw.Try again')
    }
  }

  var randomIndex = Math.floor(Math.random() * possibleMoves.length);
  game.move(possibleMoves[randomIndex]);
  board.position(game.fen());
};

var onDrop = function(source, target) {

  var move = game.move({
    from: source,
    to: target,
    promotion: 'q'
  });


  if (move === null) return 'snapback';


  window.setTimeout(makeRandomMove, 250);
};


var onSnapEnd = function() {
  board.position(game.fen());
};

var cfg = {
  draggable: true,
  position: fen_str,
  onDragStart: onDragStart,
  onDrop: onDrop,
  onSnapEnd: onSnapEnd
};

board = ChessBoard('board', cfg);
//--- end example JS ---
$('#flipOrientationBtn').on('click', board.flip);
  $('#againBtn').on('click', function() {
    board.position(fen_str)
    game = new Chess(fen_str + ' w KQkq - 0 1');
  })
}; // end init()
$(document).ready(init_play_with_computer);
