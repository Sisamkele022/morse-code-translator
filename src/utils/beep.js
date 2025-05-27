// src/utils/beep.js
import { Howl } from "howler";

const dotSound = new Howl({ src: ["/sounds/dot.mp3"] });
const dashSound = new Howl({ src: ["/sounds/dash.mp3"] });

export function playMorse(morseCode) {
  const symbols = morseCode.split("");
  let delay = 0;

  symbols.forEach((symbol) => {
    if (symbol === ".") {
      setTimeout(() => dotSound.play(), delay);
      delay += 200;
    } else if (symbol === "-") {
      setTimeout(() => dashSound.play(), delay);
      delay += 400;
    } else {
      delay += 300; // pause between letters
    }
  });
}
