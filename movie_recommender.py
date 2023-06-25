from pyspark.sql import SparkSession
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.sql.functions import col


def load_movie_data(spark, filepath):
    """
    Carga los datos de películas desde un archivo CSV utilizando Spark y retorna un DataFrame.
    """
    return spark.read.csv(filepath, header=True, inferSchema=True)


def train_als_model(data):
    """
    Entrena un modelo ALS (Alternating Least Squares) en los datos de películas.
    Retorna el modelo entrenado.
    """
    als = ALS(userCol="userId", itemCol="movieId", ratingCol="rating", coldStartStrategy="drop")
    model = als.fit(data)
    return model


def evaluate_model(model, test_data):
    """
    Evalúa el rendimiento del modelo utilizando un conjunto de datos de prueba.
    Retorna la métrica de evaluación (RMSE en este caso).
    """
    predictions = model.transform(test_data)
    evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating", predictionCol="prediction")
    rmse = evaluator.evaluate(predictions)
    return rmse


def recommend_movies(model, user_id, num_recommendations):
    """
    Genera recomendaciones de películas para un usuario específico.
    Retorna un DataFrame con las recomendaciones.
    """
    user_recs = model.recommendForUserSubset(user_id, num_recommendations)
    return user_recs


if __name__ == "__main__":
    # Crear una sesión de Spark
    spark = SparkSession.builder.appName("MovieRecommender").getOrCreate()

    # Cargar los datos de películas desde el archivo CSV
    movie_data = load_movie_data(spark, "movies.csv")

    # Dividir los datos en conjuntos de entrenamiento y prueba
    (training_data, test_data) = movie_data.randomSplit([0.8, 0.2])

    # Entrenar el modelo ALS
    model = train_als_model(training_data)

    # Evaluar el rendimiento del modelo en los datos de prueba
    rmse = evaluate_model(model, test_data)
    print(f"RMSE: {rmse}")

    # Ejemplo de recomendaciones para un usuario específico
    user_id = 1  # Reemplaza '1' con el ID del usuario deseado
    num_recommendations = 5
    recommendations = recommend_movies(model, user_id, num_recommendations)

    # Imprimir las recomendaciones para el usuario
    print(f"Recomendaciones para el usuario {user_id}:")
    recommendations.show(truncate=False)

    # Detener la sesión de Spark
    spark.stop()