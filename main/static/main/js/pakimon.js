// setInterval(function() {
//     pakimon.click();
//
// }, 20000);
//
// pakimon.onclick = function() {
//     var start = Date.now(); // сохранить время начала
//
//     var timer = setInterval(function() {
//         // вычислить сколько времени прошло из opts.duration
//         var timePassed = Date.now() - start;
//
//         pakimon.style.left = timePassed / 5 + 'px';
//
//         if (timePassed > 5000) clearInterval(timer);
//
//     }, 20);
// }