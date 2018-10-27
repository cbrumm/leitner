def leitner_box(num_new_cards=5, forgetting_rate=0.05, num_days_to_learn=365):
  """Simulates a specific implementation of the  Leitner System for memorizing.
  """
  cards = [0 for x in range(8)]
  repeat_every = [2**x for x in range(7)]
  for day in range(1, num_days_to_learn+1):
    cards[0] += num_new_cards  # new cards to learn
    stack_index_back_to_front = range(7)
    stack_index_back_to_front.reverse()
    # we learn from the back stack so we repeat wrong cards again right away
    for stack_index in stack_index_back_to_front:
      if day % repeat_every[stack_index] == 0:
      	# if we forget more than half a card, we forget 1
        cards_we_forget = round(cards[stack_index] * forgetting_rate, 0)
        cards_we_remember = cards[stack_index] - cards_we_forget
        cards[stack_index] = 0
        cards[stack_index+1] += cards_we_remember
        cards[0] += cards_we_forget
    # we always empty the first box
    cards[1] += cards[0]
    cards[0] = 0
    print "day=%d, cards=%s" % (day, cards)
