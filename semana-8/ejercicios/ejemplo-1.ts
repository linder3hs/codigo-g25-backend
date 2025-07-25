// Tipos de datos?

/**
 * Tipos primitvos:
 * string, number, boolean, null, undefined
 */

let nombre: string = "Linder";
let numeroDeAlumnos: number = 5;
let isActive: boolean = false;

// Arreglo con multiples tipos: any
// const nombres = [true, 10, "Linder"];

const nombres: string[] = ["Pepe", "Juan", "Lucho"];
// number[]
const notas: Array<number> = [10.5, 11, 20, 13.4];

// Podemos tipar parametros e indicar que tipo retornanos
function sumar(n1: number, n2: number): string {
  return `La suma es: ${n1 + n2}`;
}

sumar(10, 11);

type StringOrNull = string | null;

let username: StringOrNull = null;
username = "linder3hs";

// cundo una variable o parametro tiene el simbolo "?" es opcional
function saludar(nombre: string, edad?: number) {
  const edadMessage = edad ? ` y tengo ${edad} años.` : ".";
  return `Hola me llamo ${nombre}${edadMessage}`;
}

console.log(saludar("Juan"));
console.log(saludar("Pepe", 20));

interface IPerson {
  nombre: string;
  apellido: string;
  direccion: string;
  celular: number;
  esProgramador?: boolean;
  skills: string[];
}

const persona: IPerson = {
  nombre: "Linder",
  apellido: "Hassinger",
  direccion: "Av siempre 123",
  celular: 9999999,
  skills: ["React", "TS", "JS", "Python"],
};

const persona2: IPerson = {
  nombre: "Juan",
  apellido: "Perez",
  direccion: "Av mi casa 123",
  celular: 888888,
  skills: ["Java", "PHP", "Python"],
  esProgramador: true,
};

const personas: IPerson[] = [];
personas.push({
  nombre: "Juan",
  apellido: "Perez",
  celular: 99999,
  direccion: "av mi cas",
  skills: ["JS", "TS"],
});

type State = "activo" | "pagado" | "cancelado" | "en_progreso";
type Methods = "GET" | "POST" | "PUT" | "PATCH" | "DELETE";

const currentState: State = "activo";

function makeRequest(method: Methods) {}

makeRequest("POST");
