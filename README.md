# ds-projects
Проекты DS



|Название проекта             |Задачи проекта                              |Описание проекта    |Ключевые слова| Выводы, статус проекта|
|:----------------------------|:-------------------------------------------|:------------------------------------------------------|:-------------|:-----------------|
|[Машинное обучение для текстов](https://github.com/Nataly-nb/ds-projects/blob/main/%D0%9C%D0%B0%D1%88%D0%B8%D0%BD%D0%BD%D0%BE%D0%B5%20%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B4%D0%BB%D1%8F%20%D1%82%D0%B5%D0%BA%D1%81%D1%82%D0%BE%D0%B2/%D0%9C%D0%B0%D1%88%D0%B8%D0%BD%D0%BD%D0%BE%D0%B5%20%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B4%D0%BB%D1%8F%20%D1%82%D0%B5%D0%BA%D1%81%D1%82%D0%BE%D0%B2.ipynb)| Определение токсичности комментариев|Интернет-магазин запускает новый сервис. Теперь пользователи могут редактировать и дополнять описания товаров, как в вики-сообществах. То есть клиенты предлагают свои правки и комментируют изменения других. Требуется инструмент, который будет искать токсичные комментарии и отправлять их на модерацию.|Обработка естественного языка, NLP, nltk, tf-idf| Найдена модель со значением метрики качества F1 >= 0.75: Логистическая регрессия|
|[Информационная безопасность](https://github.com/Nataly-nb/ds-projects/tree/main/Info%20Security)|Разработать модель, которая будет классифицировать трафик на нормальный и злонамеренный, включая следующие типы атак: DDoS, SQL-инъекции, брутфорс, вредоносные программы и т.д. Дополнительная задача - собрать REST API сервис.|Компания онлайн-сервис с высоким уровнем входящего трафика имеет специализированный отдел безопасности, который занимается фильтрацией и анализом трафика. Сотрудники этого отдела обратились за помощью в автоматизации выявления аномального и злонамеренного трафика.|Pandas, Numpy, REST API|Найдена модель с максимальной метрикой Accuracy = 0.9966 - RandomForestClassifier|
|Сервис Докт24 телемедицина:  [Осложнения у беременных](https://github.com/Nataly-nb/ds-projects/blob/main/Colab/Test_task_preg_risk_ipynb.ipynb)|Прогнозирование осложнений при беременности | Согласно описанию датасета, данные были собраны из различных больниц, общественных клиник и служб охраны материнского здоровья в сельских районах Бангладеш. https://archive.ics.uci.edu/dataset/863/maternal+health+risk ||Наилучшую точность показала модель CatBoostClassifier - 83%. Наибольшее влияние на риск оказывает уровень глюкозы, наименьшее - температура. |
