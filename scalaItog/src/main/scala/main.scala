import scala.io.StdIn.readLine
object StringProcessor {
// сделали неизменяемую переменную result, заменили циклы на встроенные функции filter и map
  def processStrings(strings: List[String]): List[String] = {
    val result = strings.filter(_.length > 3).map(_.toUpperCase)
    result
  }
// функция чтения строки в список
  def read_String(str: String): List[String] = {
    val result = str.split(" ").toList
    result
  }
  def main(args: Array[String]): Unit = {
    val str = scala.io.StdIn.readLine() // чтобы можно было ввести данные как строку(а не задавать лист в ручную)
    val processedStrings = processStrings(read_String(str))
    println(s"Processed strings: $processedStrings")
  }
}
