import neat
import pickle
from flappy import FlappyBirdApp


def main():
    config = neat.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        'config'
    )

    genomes = pickle.load(open('winner.pkl', 'rb'))

    flappy = FlappyBirdApp([genomes], config)
    flappy.play()
    result = flappy.crash_info

    for r, _ in result:
        print(r['score'])


if __name__ == "__main__":
    main()
