answers = ['is', 'am', 'in']

print("Привет! Предлагаю проверить свои знания английского! Наберите 'ready', чтобы начать!")
if input() == "ready":
  good_answer = 0

  for idх in range(len(questions)):
      print(questions[idх])
      user_answer = input()
      if user_answer.lower() == answers[idх]:
          good_answer += 1
          for idх in range(len(questions)):
              print(questions[idх])
              user_answer = input()
              if user_answer.lower() == answers[idх]:
                  good_answer += 1

                    print("Правильный ответ!")
              else:
                  print(f"Неправильно. Правильный ответ:{answers[idх]}")
          print("Правильный ответ!")
      else:
          print(f"Неправильно. Правильный ответ:{answers[idх]}")
  print(f'Вот и все! Вы ответили на {good_answer} вопросов из {len(questions)} верно,'
        f' это {round(good_answer / len(questions)) * 100,2} процентов, такие дела!')
else:
  print("Кажется, вы не хотите играть. Очень жаль.")