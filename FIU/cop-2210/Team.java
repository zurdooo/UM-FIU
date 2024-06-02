public class Team {
   private String name;
   private int wins;
   private int losses;
   
   
   //       setName(), setWins(), setLosses()
   public void setName(String name){
      this.name = name;
   }
   public void setWins(int win){
      this.wins = win;
   }
   public void setLosses(int loss){
      this.losses = loss;
   }
   
   //       getName(), getWins(), getLosses()
   public String getName(){
      return name;
      
   }
   public int getWins(){
      return wins;
   }
   public int getLosses(){
      return losses;
   }
   
   public double getWinPercentage() {
      return (double)wins / (wins + losses);
   }
   
   public void printStanding() {
        double winPercentage = getWinPercentage();
        System.out.printf("%.2f\n", "Win percentage: ", winPercentage);
        if (winPercentage >= 0.5) {
            System.out.println(" Winning average");
        } else {
            System.out.println(" Losing average");
        }
    }
}