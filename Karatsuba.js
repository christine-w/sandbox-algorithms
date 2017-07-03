/*--------------------------------------------------------------
/ KaratsubaMultiply
/ Input: two string representations of integers, str1 and str2
/ Output: product of two arguments (i.e., str1 * str2) as a string
/
/   1) Multiplies using a recursive implementatin of the Karatsuba algorithm
/   TODO: Handles numbers lengths that are not a power of 2
/   TODO: Handles different number lengths
/   TODO: Handles invalid input
/   TODO: Handles negative numbers
/
/--------------------------------------------------------------*/
function KaratsubaMultiply(str1, str2, debug) {
	var strMath = require('./stringMath');
	
  if (str1.length == 1 || str2.length == 1) {
	debug && console.log('base case -- str1: ' + str1 + ' str2: ' + str2);
    return String(parseInt(str1) * parseInt(str2));
  }
  
  var n = str1.length;
  debug && console.log('str1: ' + str1 + ' str2: ' + str2);
  debug && console.log('length: ' + n + ' n/2: ' + n/2);
  
  var a = str1.substring(0, n/2);
  var b = str1.substring(n/2);
  var c = str2.substring(0, n/2);
  var d = str2.substring(n/2);  
  debug && console.log('a: ' + a);
  debug && console.log('b: ' + b);
  debug && console.log('c: ' + c);
  debug && console.log('d: ' + d);
  
  var ac = KaratsubaMultiply(a,c);
  //var adPlusbc = KaratsubaMultiply(strMath.addStringNumbers(a,b), strMath.addStringNumbers(c,d));
  var adPlusbc = strMath.addStringNumbers(KaratsubaMultiply(a,d), KaratsubaMultiply(b,c));
  var bd = KaratsubaMultiply(b,d);
  debug && console.log('ac: ' + ac);
  debug && console.log('adPlusbc: ' + adPlusbc);
  debug && console.log('bd: ' + bd);

  return strMath.addStringNumbers(strMath.addStringNumbers(ac + '0'.repeat(n), adPlusbc + '0'.repeat(n/2)), bd);

}

console.log('Recursive Karatsuba Multiplication');
//console.log(KaratsubaMultiply(2,3)); //expect 6
//console.log(KaratsubaMultiply('11','12')); //expect '132'
//console.log(KaratsubaMultiply('1234','5678',false)); //expect '7006652'
//console.log(KaratsubaMultiply('1204','5678',false)); //expect '6836312'

console.log('-----');

a = '3141592653589793238462643383279502884197169399375105820974944592';
b = '2718281828459045235360287471352662497757247093699959574966967627';
console.log(KaratsubaMultiply(a,b, true));

/*

a = '31415926535897932384626433832795';
b = '02884197169399375105820974944592';
console.log(KaratsubaMultiply(a,b, true));

*/

/*
Attempt 1: 8539624221663566055463550869546474484934868435764812930679590927057641024892184848617674971115249063013374895771951806582723184
Attempt 2: 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184
*/


