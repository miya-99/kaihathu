using System;
using System.Drawing;
using System.Windows.Forms;
using AForge.Video;
using AForge.Video.DirectShow;
using OpenCvSharp;
using ZXing;

namespace QRCodeReaderApp
{
    public partial class MainForm : Form
    {
        private FilterInfoCollection videoDevices;
        private VideoCaptureDevice videoSource;
        private bool DeviceExist = false;

        public MainForm()
        {
            InitializeComponent();
        }

        private void MainForm_Load(object sender, EventArgs e)
        {
            getCameraInfo();
        }

        private void getCameraInfo()
        {
            try
            {
                // 端末で認識しているカメラデバイスの一覧を取得
                videoDevices = new FilterInfoCollection(FilterCategory.VideoInputDevice);
                cmbCamera.Items.Clear();

                if (videoDevices.Count == 0)
                    throw new ApplicationException();

                foreach (FilterInfo device in videoDevices)
                {
                    // カメラデバイスの一覧をコンボボックスに追加
                    cmbCamera.Items.Add(device.Name);
                    cmbCamera.SelectedIndex = 0;
                    DeviceExist = true;
                }
            }
            catch (ApplicationException)
            {
                DeviceExist = false;
                cmbCamera.Items.Add("Deviceが存在していません。");
            }
        }

        private void btnExec_Click(object sender, EventArgs e)
        {
            if (btnExec.Text == "開始")
            {
                if (cmbCamera.Items.Count == 0)
                {
                    MessageBox.Show("カメラがありません。", "実行エラー");
                    return;
                }

                if (DeviceExist)
                {
                    videoSource = new VideoCaptureDevice(videoDevices[cmbCamera.SelectedIndex].MonikerString);
                    videoSource.NewFrame += new NewFrameEventHandler(videoRendering);
                    this.CloseVideoSource();
                    videoSource.Start();
                    btnExec.Text = "停止";
                }
            }
            else
            {
                if (videoSource.IsRunning)
                {
                    this.CloseVideoSource();
                    btnExec.Text = "開始";
                }
            }
        }

        private void videoRendering(object sender, NewFrameEventArgs eventArgs)
        {
            Bitmap img = (Bitmap)eventArgs.Frame.Clone();
            try
            {
                qrRead(img);
                pictureBoxCamera.Image = img;
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message + Environment.NewLine + ex.StackTrace);
            }
        }

        private void qrRead(System.Drawing.Image image)
        {
            try
            {
                Bitmap myBitmap = new Bitmap(image);
                string text = string.Empty;

                using (Mat imageMat = OpenCvSharp.Extensions.BitmapConverter.ToMat(myBitmap))
                {
                    // QRコードの解析
                    BarcodeReader reader = new BarcodeReader();

                    for (int i = 0; i < 5; i++)
                    {
                        int filterSize = i * 2 + 1