package debitos;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class Main extends Application{
    @override
    public void start(Stage primaryStage)throws Exception{
        Parent root = FXMLLoader.load(getClass().getResource("view.telaExemplo.fxml"));
        primaryStage.setTitle("teste");
        primaryStage.setScene(new Scene(root));
        primaryStage.show();
    }
    
    public void main(String[] args){launch (args);}

}
