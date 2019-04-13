package com.example.braincode2019;

        import android.app.Activity;
        import android.app.DatePickerDialog;
        import android.os.Bundle;
        import android.util.DisplayMetrics;

public class PopUpDataPicker extends Activity {



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_pop_up_data_picker);

        DisplayMetrics dm  = new DisplayMetrics();
        getWindowManager().getDefaultDisplay().getMetrics(dm);

        int width = dm.widthPixels;
        int height = dm.heightPixels;

        getWindow().setLayout((int)(width*.8),(int)(height*.6));
    }

}
