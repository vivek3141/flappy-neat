import neat
import pickle
import sys

sys.path.append("./Game")
from flappy import FlappyBirdApp


def main():
    config = neat.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        'config'
    )
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    winner = p.run(eval_genomes, n=50)
    pickle.dump(winner, open('winner.pkl', 'wb'))


def eval_genomes(genomes, config):
    idx, genomes = zip(*genomes)
    flappy = FlappyBirdApp(genomes, config)
    flappy.play()
    results = flappy.crash_info
    top_score = 0
    for result, genomes in results:

        score = result['score']
        distance = result['distance']
        energy = result['energy']

        fitness = score * 3000 + 0.2 * distance - energy * 1.5
        genomes.fitness = -1 if fitness == 0 else fitness
        if top_score < score:
            top_score = score

    print("Highest Score:", top_score)


if __name__ == "__main__":
    main()
