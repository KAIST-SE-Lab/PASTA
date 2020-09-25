package knowledge_layer;

import specification.AdaptationTactic;

import java.util.ArrayList;

public class TacticRepository {
    private ArrayList<AdaptationTactic> tactics;

    public TacticRepository(ArrayList<AdaptationTactic> adaptationTactics) {
        tactics = adaptationTactics;
    }

    public ArrayList<AdaptationTactic> getPossibleTactics() {
        return tactics;
    }

    public void addTactic(AdaptationTactic adaptationTactic) {
        tactics.add(adaptationTactic);
    }
}
