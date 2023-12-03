import 'dart:io';
import 'dart:math';

class ShownKubes {
  int red = 0;
  int green = 0;
  int blue = 0;
}

class Game {
  late int id;
  late List<ShownKubes> shownKubes;
}

main() {
  final my_file = new File('2023/day2.in');
  List<String> lines = my_file.readAsLinesSync();
  List<Game> games = <Game>[];
  for(String line in lines) {
    final splitted = line.split(":");
    final game_id = int.parse(splitted[0].substring(5));
    final game = Game();
    game.id = game_id;
    game.shownKubes = <ShownKubes>[];
    final grabs_list = splitted[1].split(";");
    for (String grab in grabs_list) {
      final shownKubes = ShownKubes();
      final kubes_by_color = grab.split(",");
      for (String kubes_input in kubes_by_color) {
        final splitted2 = kubes_input.trim().split(" ");
        final amount = int.parse(splitted2[0]);
        if (splitted2[1] == "red") {
          shownKubes.red = amount;
        } else if (splitted2[1] == "green") {
          shownKubes.green = amount;
        } else if (splitted2[1] == "blue") {
          shownKubes.blue = amount;
        }
      }
      game.shownKubes.add(shownKubes);
    }
    games.add(game);
  }

  final constraint = ShownKubes();
  constraint.red = 12;
  constraint.green = 13;
  constraint.blue = 14;

  List<Game> possible_games = <Game>[];
  for (Game game in games) {
    bool is_possible = true;
    for (ShownKubes shownKubes in game.shownKubes) {
      if (shownKubes.red > constraint.red || shownKubes.green > constraint.green || shownKubes.blue > constraint.blue) {
        is_possible = false;
      }
    }
    if (is_possible) {
      possible_games.add(game);
    }
  }
  int total = possible_games.fold(0, (previous, current) => previous + current.id);
  print(total);

  int power = 0;
  for (Game game in games) {

    final max_red = game.shownKubes.map((e) => e.red).reduce(max);
    final max_green = game.shownKubes.map((e) => e.green).reduce(max);
    final max_blue = game.shownKubes.map((e) => e.blue).reduce(max);
    power += max_red * max_green * max_blue;
  }

  print(power);
  

}