import 'dart:io';

main() {

  final digit_pattern = RegExp(r'\d');
  final my_file = new File('2023/day1.in');
  int total = 0;
  List<String> lines = my_file.readAsLinesSync();
  // for (String line in lines) {
  //   var matches = digit_pattern.allMatches(line);
  //   var digit = "${matches.first[0]!}${matches.last[0]!}";
  //   print(digit);
  //   total += int.parse(digit);
  // }
  // print(total);

  for (String line in lines) {
    var fixed_line = line.replaceAll(RegExp(r'one'), 'one1one').replaceAll(RegExp(r'two'), 'two2two').replaceAll(RegExp(r'three'), 'three3three').replaceAll(RegExp(r'four'), 'four4four').replaceAll(RegExp(r'five'), 'five5five').replaceAll(RegExp(r'six'), 'six6six').replaceAll(RegExp(r'seven'), 'seven7seven').replaceAll(RegExp(r'eight'), 'eight8eigth').replaceAll(RegExp(r'nine'), 'nine9nine');
    var matches = digit_pattern.allMatches(fixed_line);
    var digit = "${matches.first[0]!}${matches.last[0]!}";
    print(digit);
    total += int.parse(digit);
  }
  print(total);

}