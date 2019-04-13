package com.example.braincode2019;

        import android.app.Activity;
        import android.content.Intent;
        import android.os.Bundle;
        import android.util.DisplayMetrics;
        import android.view.View;
        import android.widget.AdapterView;
        import android.widget.ArrayAdapter;
        import android.widget.EditText;
        import android.widget.Spinner;

        import java.util.ArrayList;
        import java.util.List;

public class PopUpDataPicker extends Activity {

    EditText et;
    Spinner spiner;
    ArrayAdapter<String> arrayAdapter;
    List<String> list;
    String[] items = {""};
    String dayS, time;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_pop_up_data_picker);

        DisplayMetrics dm = new DisplayMetrics();
        getWindowManager().getDefaultDisplay().getMetrics(dm);

        int width = dm.widthPixels;
        int height = dm.heightPixels;

        getWindow().setLayout((int) (width * .8), (int) (height * .6));

        spiner = findViewById(R.id.spinner);
        et = findViewById(R.id.et);
        list = new ArrayList<>();
        items = getResources().getStringArray(R.array.week);
        arrayAdapter = new ArrayAdapter<>(getApplicationContext(), android.R.layout.simple_spinner_dropdown_item, items);

        spiner.setAdapter(arrayAdapter);

        spiner.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
                switch (position) {
                    case 1:
                        dayS = "SUNDAY";
                        break;
                    case 2:
                        dayS = "MONDAY";
                        break;
                    case 3:
                        dayS = "TUESDAY";
                        break;
                    case 4:
                        dayS = "WEDNESDAY";
                        break;
                    case 5:
                        dayS = "THURSDAY";
                        break;
                    case 6:
                        dayS = "FRIDAY";
                        break;
                    case 7:
                        dayS = "SATURDAY";
                        break;
                }
            }

            @Override
            public void onNothingSelected(AdapterView<?> parent) {

            }
        });
    }

    public void ok(View view) {
        time = et.getText().toString();
        Intent intent = new Intent();
        intent.putExtra("day", dayS);
        intent.putExtra("time", time);
        setResult(RESULT_OK,intent);
        finish();
    }
}
