
/*
-------DOLAR OFICIAL--------
*/
var oficialPrecioCompra = document.getElementById('oficialPrecioCompra');
var oficialPrecioVenta = document.getElementById('oficialPrecioVenta');
var oficialVariacion = document.getElementById('oficialVariacion');

/*
-------DOLAR BLUE-----------
*/
var blueCompra = document.getElementById('blueCompra');
var blueVenta = document.getElementById('blueVenta');
var blueVariacion = document.getElementById('blueVariacion');

/*
-------CONTADO CON LIQUI------
*/
var compraLiqui = document.getElementById('compraLiqui');
var ventaLiqui = document.getElementById('ventaLiqui');
var variacionLiqui = document.getElementById('variacionLiqui');

/*
------DOLAR PROMEDIO------
*/
var compraPromedio = document.getElementById('compraPromedio');
var ventaPromedio = document.getElementById('ventaPromedio');
var variacionPromedio = document.getElementById('variacionPromedio');

/*
------DOLAR BOLSA-------
*/
var compraBolsa = document.getElementById('compraBolsa');
var ventaBolsa = document.getElementById('ventaBolsa');
var variacionBolsa = document.getElementById('variacionBolsa');

/*
------DOLAR TURISTA-----
*/
var ventaTurista = document.getElementById('ventaTurista');
var variacionTurista = document.getElementById('variacionTurista');

    let url = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'
    fetch('https://www.dolarsi.com/api/api.php?type=valoresprincipales')
    .then(res => res.json())
    .then(data => {
        console.log(data);
        /* --- Dolar Oficial---*/
        oficialPrecioCompra.textContent = "$"+data[0].casa.compra;
        oficialPrecioVenta.textContent = "$"+data[0].casa.venta;
        oficialVariacion.textContent = data[0].casa.variacion;

        /* --- Dolar Blue ---*/ 
        blueCompra.textContent =  "$"+data[1].casa.compra;
        blueVenta.textContent = "$"+ data[1].casa.venta;
        blueVariacion.textContent = data[1].casa.variacion;

        /* --- Contado con Liqui ---*/ 
        compraLiqui.textContent = "$"+ data[3].casa.compra;
        ventaLiqui.textContent = "$"+ data[3].casa.venta;
        variacionLiqui.textContent = data[3].casa.variacion;

        /* --- Dolar Promedio ---*/ 
        compraPromedio.textContent =  "$"+data[7].casa.compra;
        ventaPromedio.textContent =  "$"+data[7].casa.venta;
        variacionPromedio.textContent = data[7].casa.variacion;

        /* --- Dolsar Bolsa ---*/ 
        compraBolsa.textContent =  "$"+data[4].casa.compra;
        ventaBolsa.textContent =  "$"+data[4].casa.venta;
        variacionBolsa.textContent = data[4].casa.variacion;

        /* --- Dolar Turista */
        ventaTurista.textContent = "$"+data[6].casa.venta;
        variacionTurista.textContent = data[6].casa.variacion;
    })




//fecha actualizada//

var fecha = new Date();

document.getElementById("fecha").innerHTML = `Actualizado: ${fecha.toLocaleString()}`;






