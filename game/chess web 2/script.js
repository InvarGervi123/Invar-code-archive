const chessBoard = document.getElementById('chessBoard');
let selectedPiece = null;
let selectedSquare = null;
let turn = 'white'; // Track whose turn it is

const pieces = {
    white: {
        king: '♔',
        queen: '♕',
        rook: '♖',
        bishop: '♗',
        knight: '♘',
        pawn: '♙'
    },
    black: {
        king: '♚',
        queen: '♛',
        rook: '♜',
        bishop: '♝',
        knight: '♞',
        pawn: '♟'
    }
};

const initialBoard = [
    ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'],
    ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
    ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']
];

function createBoard() {
    chessBoard.innerHTML = '';
    for (let i = 0; i < 8; i++) {
        for (let j = 0; j < 8; j++) {
            const square = document.createElement('div');
            square.className = (i + j) % 2 === 0 ? 'white' : 'black';
            square.textContent = initialBoard[i][j];
            square.dataset.row = i;
            square.dataset.col = j;
            square.addEventListener('click', onSquareClick);
            chessBoard.appendChild(square);
        }
    }
}

function onSquareClick(event) {
    const square = event.target;
    const row = parseInt(square.dataset.row);
    const col = parseInt(square.dataset.col);
    if (selectedPiece) {
        if (isValidMove(parseInt(selectedSquare.dataset.row), parseInt(selectedSquare.dataset.col), row, col)) {
            movePiece(parseInt(selectedSquare.dataset.row), parseInt(selectedSquare.dataset.col), row, col);
            selectedPiece = null;
            selectedSquare = null;
            turn = turn === 'white' ? 'black' : 'white';
            createBoard();
        }
    } else if (square.textContent) {
        if ((turn === 'white' && square.textContent === square.textContent.toUpperCase()) || (turn === 'black' && square.textContent === square.textContent.toLowerCase())) {
            selectedPiece = square.textContent;
            selectedSquare = square;
        }
    }
}

function movePiece(fromRow, fromCol, toRow, toCol) {
    initialBoard[toRow][toCol] = initialBoard[fromRow][fromCol];
    initialBoard[fromRow][fromCol] = '';
}

function isValidMove(fromRow, fromCol, toRow, toCol) {
    const piece = initialBoard[fromRow][fromCol];
    const target = initialBoard[toRow][toCol];

    // Check if moving to a square occupied by own piece
    if ((piece === piece.toUpperCase() && target === target.toUpperCase()) || (piece === piece.toLowerCase() && target === target.toLowerCase())) {
        return false;
    }

    switch (piece.toLowerCase()) {
        case '♙':
            return isValidPawnMove(fromRow, fromCol, toRow, toCol, true);
        case '♟':
            return isValidPawnMove(fromRow, fromCol, toRow, toCol, false);
        // Add cases for other pieces here
    }
    return false;
}

function isValidPawnMove(fromRow, fromCol, toRow, toCol, isWhite) {
    const direction = isWhite ? -1 : 1;
    const startRow = isWhite ? 6 : 1;

    // Regular move
    if (fromCol === toCol && initialBoard[toRow][toCol] === '') {
        if (fromRow + direction === toRow) {
            return true;
        }
        if (fromRow === startRow && fromRow + 2 * direction === toRow && initialBoard[fromRow + direction][fromCol] === '') {
            return true;
        }
    }

    // Capture move
    if (Math.abs(fromCol - toCol) === 1 && fromRow + direction === toRow && initialBoard[toRow][toCol] !== '' && initialBoard[toRow][toCol] !== '') {
        // Ensure the target is an opponent's piece
        if ((isWhite && initialBoard[toRow][toCol] === initialBoard[toRow][toCol].toLowerCase()) || (!isWhite && initialBoard[toRow][toCol] === initialBoard[toRow][toCol].toUpperCase())) {
            return true;
        }
    }

    return false;
}

createBoard();
