const squares = document.getElementsByTagName('div');

let grid = [[0,0,0],[0,0,0],[0,0,0]];
let player = 1;

for(var i=0;i<9;i++){
    squares[i].addEventListener('click',(e) => {
        const square = e.target.id;

        if(grid[Math.floor(square/3)][square%3] == 0){
            grid[Math.floor(square/3)][square%3] = player;
            e.target.innerHTML = 'XO'[player-1];

            console.log(grid);

            for(var j=0;j<3;j++){
                let winx = true;
                let winy = true;
                let wind = false;
                for(var k=1;k<3;k++){
                    if(grid[j][0] == 0 || grid[j][k] != grid[j][0]) winx = false;
                    if(grid[0][j] == 0 || grid[k][j] != grid[0][j]) winy = false;

                }
                if(grid[1][1] != 0 && ((grid[0][0] == grid[1][1] && grid[2][2] == grid[1][1]) || (grid[2][0] == grid[1][1] && grid[2][0] == grid[1][1]))) wind = true;
                if(winx || winy || wind){
                    document.getElementsByTagName('main')[0].remove();
                    document.title = 'Vitória do jogador ' + player;
                }
            }

            player = 3 - player;
        }
    });
}