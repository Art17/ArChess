/**
 * Created by Artem on 11/21/2016.
 */

var init_play_with_computer = function() {

var board,
  game = new Chess();
  statusEl = $('#status'),
  pgnEl = $('#pgn');


var onDragStart = function(source, piece, position, orientation) {
  if (game.in_checkmate() === true || game.in_draw() === true ||
    piece.search(/^b/) !== -1) {
    return false;
  }
};

var updateStatus = function() {
  var status = '';

  var moveColor = 'White';
  if (game.turn() === 'b') {
    moveColor = 'Black';
  }

  if (game.in_checkmate() === true) {
    status = 'Game over, ' + moveColor + ' is in checkmate.';
  }

  else if (game.in_draw() === true) {
    status = 'Game over, drawn position';
  }

  else {
    status = moveColor + ' to move';

    if (game.in_check() === true) {
      status += ', ' + moveColor + ' is in check';
    }
  }

  statusEl.html(status);
  pgnEl.html(game.pgn());
};

var makeRandomMove = function() {
  var possibleMoves = game.moves();

  if (possibleMoves.length === 0) return;

  var randomIndex = Math.floor(Math.random() * possibleMoves.length);
  game.move(possibleMoves[randomIndex]);
  board.position(game.fen());
  updateStatus();
};

var onDrop = function(source, target) {

  var move = game.move({
    from: source,
    to: target,
    promotion: 'q'
  });

  if (move === null) return 'snapback';
  updateStatus();
  window.setTimeout(makeRandomMove, 250);
};


var onSnapEnd = function() {
  board.position(game.fen());
};

var cfg = {
  draggable: true,
  position: 'start',
  onDragStart: onDragStart,
  onDrop: onDrop,
  onSnapEnd: onSnapEnd
};
board = ChessBoard('board', cfg);

  $('#showOrientationBtn').on('click', function() {
  console.log("Board orientation is: " + board.orientation());
});

$('#flipOrientationBtn').on('click', board.flip);

$('#whiteOrientationBtn').on('click', function() {
  board.orientation('white');
});

$('#blackOrientationBtn').on('click', function() {
  board.orientation('black');
});

};