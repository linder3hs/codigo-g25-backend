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
