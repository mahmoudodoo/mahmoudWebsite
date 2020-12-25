// Restart Game Button
var restart = document.querySelector('#bRest');
// Grabs all the squares
var squares = document.querySelectorAll('td')
// Marker 
var marker = 'X'
// Grabs all  rows
var rows = document.querySelectorAll('tr')
// Winning
var winner = false;

var rowId = 0;
// Init Array
var array = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
];

function getWinner(){
    var sum =0;

    // check rows ... 
    for (var i = 0 ; i< 3 ; i++ ){
        sum = array[i][0] + array[i][1] +array[i][2];
        if(sum == 3){return true;}
        
    };

    // Check columns ...
    for (var i = 0 ; i< 3 ; i++ ){
        sum = array[0][i] + array[1][i] +array[2][i];
        if(sum == 3){return true;}
    };

    // Check diagonals ....
    sum = array[0][0]+ array[1][1] + array[2][2];
    if(sum == 3){return true;}

    sum = array[2][0]+ array[1][1] + array[0][2];
    if(sum == 3){
        return true;
    }
    
    return false;

}; 



// Clear all squares
function clearBord(){
    for (var i =0 ; i < squares.length; i++){
        squares[i].textContent ='';
    }
  
}

// Add Event listener for restart button
restart.addEventListener('click',clearBord);


// Create Change Marker function
function changeMarker(){
    this.textContent = marker;
    if(marker == 'X'){
        marker='O';
    }else if (marker == 'O'){
        marker = 'X';
    }
    

    // update array ...
    if(this.textContent === 'X'){
        array[rowId][this.cellIndex] = 1
    }else if(this.textContent === 'O'){
        array[rowId][this.cellIndex] = -1
    }
    console.log(array[rowId][this.cellIndex])
    this.winner =  getWinner()
    console.log(winner)

    if(winner){
        alert(this.textContent + "     Winner!!!")
    }
    


}

for (var i =0 ; i < squares.length; i++){
    squares[i].addEventListener('click',changeMarker);
    
}

function setRowId(){
    rowId = this.rowIndex;
}

for (var i =0 ; i < rows.length; i++){
    rows[i].addEventListener('click',setRowId);
    
}

    
function printArray(){
    for (var i in array) 
{
   console.log("row " + i);
   for (var j in array[i]) 
     {
      console.log(" " + array[i][j]);
     }
}

}