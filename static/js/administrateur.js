// theadEnseignant=["Id","Prenome","Nom","Email","Adresse","Nb.ModelEnseigne"]
// theadEtudiant=["Id","Prenome","Nom","Email","Adresse","Filier"]
// theadModel=["Id","titre","fliere","Enseigne","nombre de heur"]
// table=document.getElementById('table');

// function suppremierFilsElement(element){
//     while (element.firstChild) {
//         element.removeChild(element.firstChild);
//     }
// }

// function thead(l){
//     // tr=document.createElement('tr')
//     // for(i=0;i<l.length;i++){
//         // th=document.createElement("th")
//         // th.textContent=l[i]
//         // tr.appendChild(th)
//     // }
//     fetch("admin_app\\administration\\enseignant.html")
//     table.appendChild();
// }
// function enseignant(){
//     suppremierFilsElement(table)
//     thead(theadEnseignant)
//     console.log("aggoub")
//     for(j=0;j<10;j++){
//         tr=document.createElement('tr')
//         for(i=0;i<theadEnseignant.length;i++){
//             td=document.createElement("td")
//             td.textContent="ayyoub "+i
//             tr.appendChild(td)  
//         }
//         table.appendChild();       
//     }
// }
// function Etudiant(){
//     suppremierFilsElement(table)
//     thead(theadEtudiant)
//     console.log("aggoub")
//     for(j=0;j<10;j++){
//         tr=document.createElement('tr')
//         for(i=0;i<theadEtudiant.length;i++){
//             td=document.createElement("td")
//             td.textContent="Etudiant "+i
//             tr.appendChild(td)  
//         }
//         table.appendChild(tr);       
//     }
// }
// function Model(){
//     suppremierFilsElement(table)
//     thead(theadModel)
//     console.log("aggoub")
//     for(j=0;j<10;j++){
//         tr=document.createElement('tr')
//         for(i=0;i<theadModel.length;i++){
//             td=document.createElement("td")
//             td.textContent="Model "+i
//             tr.appendChild(td)  
//         }
//         table.appendChild(tr);       
//     }
// }
// function chageurBackground(span){
//     listSpan=document.getElementsByName("lisidebar")
//     for(i=0;i<listSpan.length;i++){
//         listSpan[i].style.background="#666"
//         listSpan[i].style.color="#00a84f"

//     }
//     span.style.background="transparent"
//     span.style.color="#fff"

// }
// enseignant()