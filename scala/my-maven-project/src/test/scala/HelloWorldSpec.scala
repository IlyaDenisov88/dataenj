import org.scalatest.flatspec.AnyFlatSpec

class HelloWOrldSpec extends AnyFlatSpec {
	"The add function" should "return the sum of two numbers" in {
		assert(HelloWorld.add(2, 3) === 5)
	}
}
