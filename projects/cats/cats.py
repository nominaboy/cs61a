"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    result_list = []
    for p in paragraphs:
        if select(p):
            result_list.append(p)
    if k < len(result_list):
        return result_list[k]
    else:
        return ''
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def sel_func(paragraph):
        words_for_select = split(remove_punctuation(paragraph))
        for words_in_topic in topic:
            for words_in_paragraph in words_for_select:
                if words_in_topic == lower(words_in_paragraph):
                    return True
        return False
    return sel_func
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    denominator_acc = len(typed_words)
    counter_upper_bound = min(len(typed_words), len(reference_words))
    counter = 0
    numerator = 0
    if denominator_acc == 0:
        return 0.0
    while counter < counter_upper_bound:
        if typed_words[counter] == reference_words[counter]:
            numerator += 1
        counter += 1
    return numerator * 100 / denominator_acc
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    return 60 / elapsed * (len(typed) / 5)
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    if user_word in valid_words:
        return user_word
    else:
        min_diff = float('inf')
        for w in valid_words:
            words_diff = diff_function(user_word, w, limit)
            if words_diff < min_diff:
                min_diff_word = w
                min_diff = words_diff
        if min_diff > limit:
            return user_word
        else:
            return min_diff_word



    # END PROBLEM 5


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    # assert False, 'Remove this line'

    # length_diff = abs(len(start) - len(goal))
    # counter_upper = min(len(start), len(goal))
    # words_counter = 0
    # diff_counter = 0
    # while words_counter < counter_upper:
    #     if start[words_counter] != goal[words_counter]:
    #         diff_counter += 1
    #     words_counter += 1
    # return diff_counter + length_diff
    def shifty_shifts_helper(start, goal, limit, num):
        length_diff = abs(len(start) - len(goal))
        if num + length_diff > limit:
            return limit + 1
        if len(start) == 0 or len(goal) == 0:
            return num + length_diff
        if start[0] != goal[0]:
            num += 1
        return shifty_shifts_helper(start[1:], goal[1:], limit, num)

    return shifty_shifts_helper(start, goal, limit, num = 0)




    # END PROBLEM 6


def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    # assert False, 'Remove this line'
    def pawssible_patches_helper(start, goal, limit, num):
        length_diff = abs(len(start) - len(goal))
        if (length_diff + num) > limit: # Fill in the condition
            # BEGIN
            "*** YOUR CODE HERE ***"
            return limit + 1
            # END

        elif len(start) == 0 or len(goal) == 0: # Feel free to remove or add additional cases
            # BEGIN
            "*** YOUR CODE HERE ***"
            return num + length_diff
            # END

        elif start[0] == goal[0]:
            return pawssible_patches_helper(start[1:], goal[1:], limit, num)

        else:
            """
            add_diff = pawssible_patches_helper(start, goal[1:], limit, num) # Fill in these lines
            remove_diff = pawssible_patches_helper(start[1:], goal, limit, num)
            substitute_diff = pawssible_patches_helper(start[1:], goal[1:], limit, num)
            """
            # BEGIN
            "*** YOUR CODE HERE ***"
            num += 1
            return min(pawssible_patches_helper(start, goal[1:], limit, num),
                       pawssible_patches_helper(start[1:], goal, limit, num),
                       pawssible_patches_helper(start[1:], goal[1:], limit, num))

    return pawssible_patches_helper(start, goal, limit, num = 0)


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    upper_bound = len(typed)
    denominator = len(prompt)
    i = 0
    while i < upper_bound:
        if typed[i] == prompt[i]:
            i += 1
        else:
            break
    progress = i / denominator
    send(dict([('id', user_id), ('progress', progress)]))
    print(progress)

    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"

    items = len(times_per_player)
    words_length = len(times_per_player[0])
    game_timelist =[]
    for i in range(items):
        game_timelist.append([])
        for j in range(words_length - 1):
            game_timelist[i].append(times_per_player[i][j+1] - times_per_player[i][j])
    return game(words, game_timelist)



    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    player_indices = range(len(all_times(game)))  # contains an *index* for each player
    word_indices = range(len(all_words(game)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    result_list = []
    for i in player_indices:
        result_list.append([])
    for word_index in word_indices:
        shortest_time = float('inf')
        fastest_player = 0
        for player_index in player_indices:
            current_time = time(game, player_index, word_index)
            if current_time < shortest_time:
                shortest_time = current_time
                fastest_player = player_index
        result_list[fastest_player].append(word_at(game, word_index))
    return result_list
    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)