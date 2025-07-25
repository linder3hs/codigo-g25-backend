/**
 * Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o
 * falso (Bool) según sean o no anagramas.
 * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra
 * inicial.
 * NO hace falta comprobar que ambas palabras existan.
 * Dos palabras exactamente iguales no son anagrama.
 *
 * "roma" -> amor
 * "omar" -> amor
 *
 * hola -> ahlo
 * hole -> ehlo
 */

function sortWord(word: string): string {
  return word.toLowerCase().split("").sort().join("");
}

function isAnagram(word1: string, word2: string): boolean {
  if (word1.toLowerCase() === word2.toLowerCase()) return false;

  return sortWord(word1) === sortWord(word2);
}

console.log(isAnagram("roma", "omar"));
console.log(isAnagram("rOma", "omar"));
console.log(isAnagram("hola", "helo"));
console.log(isAnagram("codigo", "codigo"));

console.log("======PROBLEMA2======");

/**
 * Enunciado: Escribe un programa que muestre por consola
 * (con un print)
 * los números de 1 a 100 (ambos incluidos y con un
 * salto de línea entre cada impresión),
 * sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 *
 */

function validateMultipleOfNumber(number: number): string {
  const mutiplo3 = number % 3 === 0;
  const mutiplo5 = number % 5 === 0;

  return mutiplo3 && mutiplo5
    ? "fizzbuzz"
    : mutiplo3
    ? "fizz"
    : mutiplo5
    ? "buzz"
    : String(number);
}

function analyzeNumbers(): string {
  const result: string[] = [];

  for (let i = 1; i < 101; i++) {
    result.push(validateMultipleOfNumber(i));
  }

  return result.join("\n");
}

console.log(analyzeNumbers());

/**
 * Papá Noel 🎅 ha recibido una lista de números mágicos que representan regalos 🎁, pero algunos de ellos están duplicados y deben eliminarse para evitar confusiones. Además, los regalos deben ordenarse en orden ascendente antes de entregarlos a los elfos.

Tu tarea consiste en escribir una función que reciba una lista de números enteros (que puede incluir duplicados) y devuelva una nueva lista sin duplicados, ordenada en orden ascendente.

const gifts1 = [3, 1, 2, 3, 4, 2, 5]
const preparedGifts1 = prepareGifts(gifts1)
console.log(preparedGifts1) // [1, 2, 3, 4, 5]

const gifts2 = [6, 5, 5, 5, 5]
const preparedGifts2 = prepareGifts(gifts2)
console.log(preparedGifts2) // [5, 6]

const gifts3 = []
const preparedGifts3 = prepareGifts(gifts3)
console.log(preparedGifts3) // []
// There are no gifts, the list remains empty
 */

// function prepareGifts(numbers: number[]): number[] {
//   if (numbers.length === 0) return [];

//   const orderedArray = numbers.sort((a, b) => a - b);
//   const result: number[] = [];

//   for (let number of orderedArray) {
//     if (result.length === 0) {
//       result.push(number);
//     } else {
//       const searchNumber = result.find((item) => item === number);

//       if (!searchNumber) result.push(number);
//     }
//   }

//   return result;
// }

function prepareGifts(numbers: number[]): number[] {
  return [...new Set(numbers)].sort((a, b) => a - b);
}

console.log("\n\n\n======PROBLEMA3======");

const gifts1 = [3, 1, 2, 3, 4, 2, 5];
const preparedGifts1 = prepareGifts(gifts1);
console.log(preparedGifts1); // [1, 2, 3, 4, 5]

const gifts2 = [6, 5, 5, 5, 5];
const preparedGifts2 = prepareGifts(gifts2);
console.log(preparedGifts2); // [5, 6]

const gifts3: number[] = [];
const preparedGifts3 = prepareGifts(gifts3);
console.log(preparedGifts3); // []
