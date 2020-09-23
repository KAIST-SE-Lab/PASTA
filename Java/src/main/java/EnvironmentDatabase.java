import java.util.ArrayList;

public class EnvironmentDatabase {
    private ArrayList<EnvironmentData> historicalData;

    public EnvironmentDatabase(){
        historicalData = new ArrayList<EnvironmentData>();
    }

    public void addEnvironmentData(EnvironmentData envData){
        historicalData.add(envData);
    }

    public ArrayList<EnvironmentData> getHistoricalEnvironmentData(){
        return historicalData;
    }
}
