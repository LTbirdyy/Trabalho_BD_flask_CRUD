// Usando SWITCH

/*switch(expressao){
    case valor 1:
        break (obrigatorio esse break em cada case e no default)}

    case valor 2:
        break

    default: (caso não atenda nenhum dos casos anteriores)
        break
}
*/

let agora = new Date()
let diaSem = agora.getDate()

switch(diaSem){
    case 1,2,3,4,6:
        console.log("Dia da semana")
        break
    
    case 7,0:
        console.log("Fim de semana")
        break
    
}
console.log(diaSem)
