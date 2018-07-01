using System;
using System.Collections.Generic;
using System.IO;
using System.Windows.Forms;

namespace Translit
{
    public partial class Form1 : Form
    {
        Dictionary<string, string> arr;

        public Form1()
        {
            InitializeComponent();

            arr = new Dictionary<string, string>();

            if (!File.Exists("tr.txt"))
            {
                StreamWriter sw = new StreamWriter("tr.txt", false, System.Text.Encoding.Default);
                sw.Write("А:A\nБ:B\nВ:V\nГ:G\nД:D\nЕ:E\nЁ:E\nЖ:ZH\nЗ:Z\nИ:I\nЙ:J\nК:K\nЛ:L\nМ:M\nН:N\nО:O\nП:P\nР:R\nС:S\nТ:T\nУ:U\nФ:F\nХ:KH\nЦ:TS\nЧ:CH\nШ:SH\nЩ:SHH\nЪ:\nЫ:Y\nЬ:\nЭ:E\nЮ:YU\nЯ:YA\n" +
                    "а:a\nб:b\nв:v\nг:g\nд:d\nе:e\nё:e\nж:zh\nз:z\nи:i\nй:j\nк:k\nл:l\nм:m\nн:n\nо:o\nп:p\nр:r\nс:s\nт:t\nу:u\nф:f\nх:kh\nц:ts\nч:ch\nш:sh\nщ:shh\nъ:\nы:\nь:\nэ:e\nю:yu\nя:ya");
                sw.Close();
            }
      
            StreamReader sr = new StreamReader("tr.txt", System.Text.Encoding.Default);
            string str;
            while ((str = sr.ReadLine()) != null)
            {
                arr.Add(str.Split(':')[0], str.Split(':')[1]);
            }

            sr.Close();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string str = textBox1.Text;

            foreach (KeyValuePair<string, string> i in arr)
            {
                str = str.Replace(i.Key, i.Value);
            }

            textBox2.Text = str;
        }
    }
}
