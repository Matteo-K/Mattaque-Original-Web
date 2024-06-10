//JavaScipt Essaie

// control + / pour mettre un commentaire

/* ou 
comme ça*/

// alert("yo");
// console.log("coucou la console");
// console.log("hi boy");

/* Les variables */

let variable = "bonjour";
console.log(variable);

var vari = 5;
console.log(vari);
// let == var (var c'est le vieux JS)

const prenom = "jusine";

//const est une variable qui ne bouge pas (une constante)

// ** Les types de données **
let varia = 5;
varia++;
console.log(varia);

let x = 10;
let y = 15;

if (x > y) {
  alert("x plus grand que y");
  console.log(x, "x");
} else if (y === x) {
  // === test l'égalité de type et de contenu   (str et chiffre / entre chiffres / ...)  et == c'est sans prendre en compte le type  2 et "2" sont égaux
  alert("Ils sont égaux");
} else {
  alert("y est plus grand que x");
  console.log(y, "y");
}

// || c'est 'ou'. && c'est 'et'

if (x > y || x === y) {
  console.log("ou");
} else {
  console.log(y, "y");
}

// fonction classique
function division(b, x) {
  if (x != 0) {
    console.log(b / x);
  }
}

// fontion fléché
const fleche = (a, b) => {
  if (a > b) {
    console.log(a, "est plus grand que", b);
  } else if (a < b) {
    console.log(b, "est plus grand que", a);
  } else {
    console.log("ILS SONT EGAUX");
  }
};

// fonction recursive
const recursive = (x, liste = []) => {
  if (x === 0) {
    liste += [0];
    return console.log(liste), 0;
  } else {
    liste += [x];
    return x + recursive(x - 1, (liste += ["+"]));
  }
};
