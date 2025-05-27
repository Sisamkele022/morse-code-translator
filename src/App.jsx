import React, { useState, useEffect, useRef } from 'react';
import './App.css';

const morseCode = {
  A: '.-', B: '-...', C: '-.-.', D: '-..', E: '.', F: '..-.',
  G: '--.', H: '....', I: '..', J: '.---', K: '-.-', L: '.-..',
  M: '--', N: '-.', O: '---', P: '.--.', Q: '--.-', R: '.-.',
  S: '...', T: '-', U: '..-', V: '...-', W: '.--', X: '-..-',
  Y: '-.--', Z: '--..', '1': '.----', '2': '..---', '3': '...--',
  '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
  '9': '----.', '0': '-----', ' ': '/'
};

const reverseMorseCode = Object.fromEntries(Object.entries(morseCode).map(([k, v]) => [v, k]));

function App() {
  const [inputText, setInputText] = useState('');
  const [outputText, setOutputText] = useState('');

  const backgroundMusicRef = useRef(null);
  const dotSound = useRef(null);
  const dashSound = useRef(null);

  useEffect(() => {
    // Autoplay background music on interaction
    const startMusic = () => {
      backgroundMusicRef.current.volume = 0.3;
      backgroundMusicRef.current.loop = true;
      backgroundMusicRef.current.play().catch(() => {
        console.log('Autoplay blocked. Waiting for interaction.');
      });
      window.removeEventListener('click', startMusic);
    };

    window.addEventListener('click', startMusic);
    return () => window.removeEventListener('click', startMusic);
  }, []);

  const handleEncode = () => {
    const text = inputText.toUpperCase();
    const morse = text
      .split('')
      .map(char => morseCode[char] || '')
      .join(' ');

    setOutputText(morse);

    // Play sounds
    playMorseSound(morse);
  };

  const handleDecode = () => {
    const decoded = inputText
      .split(' ')
      .map(code => reverseMorseCode[code] || '')
      .join('');
    setOutputText(decoded);
  };

  const playMorseSound = (morse) => {
    let i = 0;

    const playNext = () => {
      if (i >= morse.length) return;
      const char = morse[i];
      if (char === '.') {
        dotSound.current.play();
      } else if (char === '-') {
        dashSound.current.play();
      }
      i++;
      setTimeout(playNext, 300);
    };

    playNext();
  };

  return (
    <div className="app-container">
      <audio ref={backgroundMusicRef} src="/sounds/background_music.mp3" />
      <audio ref={dotSound} src="/sounds/dot.mp3" />
      <audio ref={dashSound} src="/sounds/dash.mp3" />

      <h1 className="title">Morse Code Translator</h1>
      <textarea
        className="input-box"
        rows="4"
        placeholder="Enter text or Morse code"
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
      />

      <div className="button-group">
        <button className="glow-button" onClick={handleEncode}>Encode</button>
        <button className="glow-button" onClick={handleDecode}>Decode</button>
      </div>

      <div className="output-section">
        <h2>Output:</h2>
        <div className="output-box">{outputText}</div>
      </div>
    </div>
  );
}

export default App;
