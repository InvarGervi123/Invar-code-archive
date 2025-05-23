import React, { useState } from 'react';
import Chess from 'chess.js';
import Chessboard from 'chessboardjsx';

const Game = () => {
  const [game, setGame] = useState(new Chess());
  const [fen, setFen] = useState('start');

  const onDrop = ({ sourceSquare, targetSquare }) => {
    let move = game.move({
      from: sourceSquare,
      to: targetSquare,
      promotion: 'q' // promotion to a queen
    });

    if (move === null) return 'snapback';

    setFen(game.fen());
  };

  const resetGame = () => {
    const newGame = new Chess();
    setGame(newGame);
    setFen('start');
  };

  return (
    <div>
      <Chessboard
        width={600}
        position={fen}
        onDrop={onDrop}
      />
      <button onClick={resetGame}>New Game</button>
    </div>
  );
};

export default Game;
