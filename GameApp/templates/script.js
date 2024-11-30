const button1 = document.getElementById('button1');
const button2 = document.getElementById('button2');
const button3 = document.getElementById('button3');
const winMessage = document.getElementById('win-message');
const playAgainButton = document.getElementById('play-again');

let winningButton;

function playGame() {
  winningButton = Math.floor(Math.random() * 3) + 1; // Random number between 1 and 3
  resetButtons();
}

function checkWin(buttonNumber) {
  if (buttonNumber === winningButton) {
    winMessage.textContent = 'You Win!';
  } else {
    winMessage.textContent = 'You Lose!';
  }
}

function resetButtons() {
  button1.style.backgroundColor = 'gray';
  button2.style.backgroundColor = 'gray';
  button3.style.backgroundColor = 'gray';
  winMessage.textContent = '';
}

playGame();

button1.addEventListener('click', () => checkWin(1));
button2.addEventListener('click', () => checkWin(2));
button3.addEventListener('click', () => checkWin(3));

playAgainButton.addEventListener('click', () => {
  playGame();
});