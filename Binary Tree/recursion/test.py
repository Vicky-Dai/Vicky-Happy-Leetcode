import lombok.Getter;

@Getter
public class Car {
    String color;
    String manufacturer;
    String modelName;
    int year;

    Engine engine;
    Wheel frontRight;
    Wheel frontLeft;
    Wheel rearRight;
    Wheel rearLeft;

    Logo logo;

    Headlight leftHeadlight;
    Headlight rightHeadlight;

    // 构造器
    public Car(String color, String manufacturer, String modelName, int year,
               Engine engine, Wheel frontRight, Wheel frontLeft,
               Wheel rearRight, Wheel rearLeft, Logo logo,
               Headlight leftHeadlight, Headlight rightHeadlight) {
        this.color = color;
        this.manufacturer = manufacturer;
        this.modelName = modelName;
        this.year = year;
        this.engine = engine;
        this.frontRight = frontRight;
        this.frontLeft = frontLeft;
        this.rearRight = rearRight;
        this.rearLeft = rearLeft;
        this.logo = logo;
        this.leftHeadlight = leftHeadlight;
        this.rightHeadlight = rightHeadlight;
    }
}