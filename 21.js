// 1/7/2020

// 2-1 Looping a triangle

function loopTriangle() {
    let i, j, n=4;
    for (i = 0; i < n; i++) {
        let str = '';
        for (j = 0; j <= i; j++) {
            str += '#';
        }
        console.log(str);
    };
}

loopTriangle();