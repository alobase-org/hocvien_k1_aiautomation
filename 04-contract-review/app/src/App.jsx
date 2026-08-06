import React, { useState, useRef } from 'react';
import { 
  FileText, 
  UploadCloud, 
  ShieldCheck, 
  AlertTriangle, 
  Download, 
  RefreshCw, 
  CheckCircle2, 
  Sparkles, 
  FileCode2, 
  Cpu, 
  Link2,
  Zap,
  ArrowRight,
  FileCheck
} from 'lucide-react';
import mammoth from 'mammoth';
import confetti from 'canvas-confetti';

const SAMPLE_CONTRACT = `CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM
Độc lập - Tự do - Hạnh phúc
---

HỢP ĐỒNG NGUYÊN TẮC CUNG CẤP DỊCH VỤ PHẦN MỀM & AI
Số: HD-2026-UPLOAD

Hôm nay, ngày 15 tháng 03 năm 2026, tại TP. Hồ Chí Minh, chúng tôi gồm có:

BÊN A (BÊN GIAO): CÔNG TY CỔ PHẦN CÔNG NGHỆ ALOBASE
- Đại diện: Ông Nguyễn Văn Nam - Chức vụ: Giám đốc
- Địa chỉ: 123 Đường Lê Lợi, Quận 1, TP. Hồ Chí Minh
- Mã số thuế: 0312345678
- Điện thoại: 0903123456 - Email: contact@alobase.vn

BÊN B (BÊN NHẬN): CÔNG TY TNHH GIẢI PHÁP PHẦN MỀM ABC
- Đại diện: Bà Trần Thị Mai - Chức vụ: Giám đốc
- Địa chỉ: 456 Đường Nguyễn Thị Minh Khai, Quận 3, TP. Hồ Chí Minh
- Mã số thuế: 0398765432
- Điện thoại: 0918999888 - Email: info@abcsoft.com

Hai bên cùng thống nhất ký kết Hợp đồng với các điều khoản chi tiết như sau:

ĐIỀU 01: ĐỐI TƯỢNG VÀ PHẠM VI CÔNG VIỆC
Bên B thực hiện thiết kế, phát triển và triển khai hệ thống phần mềm AI Rà soát Hợp đồng theo yêu cầu kỹ thuật của Bên A. Ngoài ra Bên B phải thực hiện các công việc khác theo yêu cầu của Bên A mà không tính thêm chi phí.

ĐIỀU 02: GIÁ TRỊ HỢP ĐỒNG VÀ THỜI HẠN THANH TOÁN
- Tổng giá trị hợp đồng: 500.000.000 VNĐ (Năm trăm triệu đồng).
- Bên A sẽ thanh toán cho Bên B khi Bên A cảm thấy hoàn toàn hài lòng với tiến độ công việc trong thời hạn hợp lý.

ĐIỀU 03: NGHĨA VỤ CỦA BÊN B
Bên B có nghĩa vụ bố trí đội ngũ nhân sự chuyên trách. Bên B không được thay đổi nhân sự trong suốt quá trình dự án, nếu thay đổi sẽ bị phạt 100.000.000 VNĐ cho mỗi lần thay đổi nhân sự.

ĐIỀU 04: THỜI HẠN VÀ TIẾN ĐỘ THỰC HIỆN
Thời hạn hoàn tất công việc là 60 ngày kể từ ngày ký. Tiến độ hoàn thành là cố định bất kể thời gian Bên A phản hồi hoặc phê duyệt thông tin.

ĐIỀU 05: CHẤM DỨT HỢP ĐỒNG VÀ PHẠT VI PHẠM
Bên A có quyền đơn phương chấm dứt hợp đồng bất kỳ lúc nào mà không phải bồi thường bất kỳ khoản chi phí nào cho Bên B. Nếu Bên B vi phạm hợp đồng, Bên B sẽ bị phạt 30% tổng giá trị hợp đồng.

ĐIỀU 06: BẢO MẬT THÔNG TIN
Bên B có trách nhiệm bảo mật toàn bộ thông tin dự án vô thời hạn. Trường hợp tiết lộ thông tin, Bên B phải nộp phạt 5.000.000.000 VNĐ.

ĐIỀU 07: SỞ HỮU TRÍ TUỆ
Toàn bộ bản quyền phần mềm và source code thuộc về Bên A ngay từ thời điểm được tạo ra, bất kể Bên A đã thanh toán đủ tiền hay chưa.

ĐIỀU 08: TRÁCH NHIỆM BỒI THƯỜNG THIỆT HẠI
Bên B chịu trách nhiệm bồi thường toàn bộ thiệt hại phát sinh không giới hạn, bao gồm cả thiệt hại gián tiếp, mất cơ hội kinh doanh và suy giảm uy tín thương hiệu của Bên A.

ĐIỀU 09: ĐIỀU KHOẢN TỰ ĐỘNG GIA HẠN
Hợp đồng tự động gia hạn thêm 01 năm sau khi hết hạn, trừ khi Bên B có văn bản thông báo trước 60 ngày.

ĐIỀU 10: GIẢI QUYẾT TRANH CHẤP
Mọi tranh chấp phát sinh từ hợp đồng này sẽ được đưa ra giải quyết tại Tòa án nhân dân tỉnh Cà Mau.

ĐẠI DIỆN BÊN A                                            ĐẠI DIỆN BÊN B`;

export default function App() {
  const [webhookUrl, setWebhookUrl] = useState('/webhook/contract-review');
  const [activeTab, setActiveTab] = useState('upload'); // 'upload' | 'text'
  const [contractText, setContractText] = useState('');
  const [fileName, setFileName] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [currentStep, setCurrentStep] = useState(0);
  const [errorMsg, setErrorMsg] = useState('');
  const [downloadBlobUrl, setDownloadBlobUrl] = useState(null);
  const [downloadFileName, setDownloadFileName] = useState('');
  const [fileSize, setFileSize] = useState(0);
  const fileInputRef = useRef(null);

  const processingSteps = [
    { title: 'Chuẩn hóa & Trích xuất Văn bản', desc: 'Đọc dữ liệu file / input contract_text' },
    { title: 'Khử trùng dữ liệu (Redaction 4 Cấp)', desc: 'Ẩn PII, SĐT, Email, MST, Giá trị tài chính & Security Gate' },
    { title: 'AI Legal Analysis (Gemini 2.0)', desc: 'Trích xuất điều khoản & Đối chiếu KB Red Flags' },
    { title: 'Kiểm tra Semantic Evidence', desc: 'Xác minh trích dẫn nguyên văn (Verbatim) & Omission' },
    { title: 'Đóng gói Báo cáo Word (Nghị định 30)', desc: 'Tạo file report.docx & Trả về binary response' }
  ];

  const handleFileChange = async (e) => {
    const file = e.target.files[0];
    if (!file) return;
    setFileName(file.name);
    setErrorMsg('');

    try {
      if (file.name.endsWith('.docx')) {
        const arrayBuffer = await file.arrayBuffer();
        const result = await mammoth.extractRawText({ arrayBuffer });
        setContractText(result.value);
      } else if (file.name.endsWith('.txt')) {
        const text = await file.text();
        setContractText(text);
      } else {
        setErrorMsg('Vui lòng chọn file .docx hoặc .txt (hoặc dán trực tiếp văn bản)');
      }
    } catch (err) {
      console.error(err);
      setErrorMsg('Lỗi khi đọc file: ' + err.message);
    }
  };

  const handleLoadSample = () => {
    setContractText(SAMPLE_CONTRACT);
    setFileName('Hop_Dong_Mau_Test_RedFlags.txt');
    setActiveTab('text');
    setErrorMsg('');
  };

  const handleSubmit = async () => {
    if (!contractText.trim()) {
      setErrorMsg('Vui lòng nhập hoặc upload nội dung hợp đồng trước khi rà soát!');
      return;
    }

    setIsLoading(true);
    setErrorMsg('');
    setDownloadBlobUrl(null);
    setCurrentStep(0);

    const stepInterval = setInterval(() => {
      setCurrentStep((prev) => (prev < 4 ? prev + 1 : prev));
    }, 1500);

    try {
      // Direct relative requests through Vite proxy to bypass Ngrok HTTPS -> HTTP Mixed Content / CORS
      let targetUrl = webhookUrl;
      if (targetUrl.startsWith('http://localhost:5678')) {
        targetUrl = targetUrl.replace('http://localhost:5678', '');
      }

      const response = await fetch(targetUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          contract_text: contractText,
          contract_id: 'HD-' + new Date().getFullYear() + '-WEB'
        })
      });

      clearInterval(stepInterval);
      setCurrentStep(4);

      if (!response.ok) {
        let errMessage = response.statusText;
        try {
          const errJson = await response.json();
          errMessage = errJson.message || errJson.error || JSON.stringify(errJson);
        } catch (e) {
          errMessage = await response.text();
        }
        throw new Error(`Lỗi xử lý từ n8n Webhook (HTTP ${response.status}):\n${errMessage}`);
      }

      const contentType = response.headers.get("content-type") || "";
      if (contentType.includes("application/json")) {
        const jsonBody = await response.json();
        if (jsonBody.error || jsonBody.message) {
          throw new Error(`Lỗi xử lý AI:\n${jsonBody.message || jsonBody.error}`);
        }
      }

      const blob = await response.blob();
      if (blob.size === 0) {
        throw new Error('File trả về từ n8n Webhook rỗng (0 bytes). Kiểm tra lại respondToWebhook node!');
      }

      const url = window.URL.createObjectURL(blob);
      setDownloadBlobUrl(url);
      setFileSize(blob.size);

      const outName = fileName 
        ? `Bao_Cao_Ra_Soat_${fileName.replace(/\.[^/.]+$/, "")}.docx`
        : `Bao_Cao_Ra_Soat_Hop_Dong_${Date.now()}.docx`;
      setDownloadFileName(outName);

      const a = document.createElement('a');
      a.href = url;
      a.download = outName;
      document.body.appendChild(a);
      a.click();
      a.remove();

      confetti({
        particleCount: 80,
        spread: 70,
        origin: { y: 0.6 }
      });

    } catch (err) {
      clearInterval(stepInterval);
      console.error('Webhook Error:', err);
      let msg = err.message;
      if (err.name === 'TypeError' && err.message.includes('Failed to fetch')) {
        msg = `Không thể kết nối tới n8n Webhook tại "${webhookUrl}". Vui lòng kiểm tra:\n1. n8n đã được bật chưa (n8n start)?\n2. Workflow n8n đã bấm "Listen for test event" hoặc Active workflow chưa?\n3. Kiểm tra CORS trên n8n nếu có.`;
      }
      setErrorMsg(msg);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: '1200px', margin: '0 auto', padding: '36px 20px' }}>
      
      {/* HEADER */}
      <header style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '32px', flexWrap: 'wrap', gap: '16px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '14px' }}>
          <div style={{
            width: '48px', height: '48px', borderRadius: '14px',
            background: 'linear-gradient(135deg, #0284c7 0%, #2563eb 100%)',
            display: 'flex', alignItems: 'center', justifyContent: 'center',
            boxShadow: '0 4px 14px rgba(2, 132, 199, 0.35)'
          }}>
            <ShieldCheck size={28} color="#fff" />
          </div>
          <div>
            <h1 style={{ fontSize: '24px', fontWeight: '800', letterSpacing: '-0.5px', color: '#0f172a' }}>
              Legal AI <span className="gradient-text">Guard</span>
            </h1>
            <p style={{ color: '#64748b', fontSize: '13px', fontWeight: '500' }}>
              Hệ thống Rà soát Hợp đồng Tự động & Xuất Báo cáo DOCX qua n8n AI Workflow
            </p>
          </div>
        </div>

        {/* WEBHOOK URL CONFIG */}
        <div className="glass-card" style={{ padding: '8px 16px', display: 'flex', alignItems: 'center', gap: '10px' }}>
          <Link2 size={16} color="#0284c7" />
          <span style={{ fontSize: '12px', color: '#64748b', fontWeight: '600' }}>n8n Webhook:</span>
          <input 
            type="text" 
            value={webhookUrl}
            onChange={(e) => setWebhookUrl(e.target.value)}
            style={{
              background: '#f8fafc',
              border: '1px solid #cbd5e1',
              borderRadius: '6px',
              padding: '6px 10px',
              color: '#0284c7',
              fontSize: '12px',
              fontFamily: 'var(--font-mono)',
              fontWeight: '600',
              width: '320px',
              outline: 'none'
            }}
          />
        </div>
      </header>

      {/* MAIN CONTENT */}
      <div>
        
        {/* INPUT CARD */}
        {!downloadBlobUrl && !isLoading && (
          <div className="glass-card" style={{ padding: '28px' }}>
            
            {/* TABS */}
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px', borderBottom: '1px solid #e2e8f0', paddingBottom: '14px' }}>
              <div style={{ display: 'flex', gap: '12px' }}>
                <button 
                  className="secondary-btn"
                  onClick={() => setActiveTab('upload')}
                  style={{
                    background: activeTab === 'upload' ? '#eff6ff' : '#f8fafc',
                    borderColor: activeTab === 'upload' ? '#2563eb' : '#cbd5e1',
                    color: activeTab === 'upload' ? '#1d4ed8' : '#64748b',
                    fontWeight: activeTab === 'upload' ? '600' : '500'
                  }}
                >
                  <UploadCloud size={16} /> Tải file (.docx / .txt)
                </button>
                <button 
                  className="secondary-btn"
                  onClick={() => setActiveTab('text')}
                  style={{
                    background: activeTab === 'text' ? '#eff6ff' : '#f8fafc',
                    borderColor: activeTab === 'text' ? '#2563eb' : '#cbd5e1',
                    color: activeTab === 'text' ? '#1d4ed8' : '#64748b',
                    fontWeight: activeTab === 'text' ? '600' : '500'
                  }}
                >
                  <FileText size={16} /> Dán văn bản hợp đồng
                </button>
              </div>

              <button 
                onClick={handleLoadSample}
                className="secondary-btn"
                style={{ fontSize: '13px', color: '#b45309', background: '#fffbeb', borderColor: '#fde68a', fontWeight: '600' }}
              >
                <Sparkles size={15} color="#d97706" /> Nạp Hợp đồng Mẫu (Red Flags Test)
              </button>
            </div>

            {/* TAB CONTENT: UPLOAD */}
            {activeTab === 'upload' && (
              <div>
                <div 
                  className="drag-drop-zone"
                  onClick={() => fileInputRef.current?.click()}
                  style={{ padding: '44px 20px', textAlign: 'center' }}
                >
                  <input 
                    type="file" 
                    ref={fileInputRef} 
                    onChange={handleFileChange}
                    accept=".docx,.txt"
                    style={{ display: 'none' }} 
                  />
                  <div style={{
                    width: '64px', height: '64px', borderRadius: '50%',
                    background: '#dbeafe',
                    display: 'flex', alignItems: 'center', justifyContent: 'center',
                    margin: '0 auto 16px auto'
                  }}>
                    <UploadCloud size={32} color="#2563eb" />
                  </div>
                  <h3 style={{ fontSize: '16px', fontWeight: '700', color: '#0f172a', marginBottom: '6px' }}>
                    Kéo thả hoặc Bấm để chọn file Hợp đồng
                  </h3>
                  <p style={{ color: '#64748b', fontSize: '13px' }}>
                    Hỗ trợ định dạng Microsoft Word (<strong>.docx</strong>) hoặc Plain Text (<strong>.txt</strong>)
                  </p>
                  {fileName && (
                    <div style={{
                      marginTop: '16px', display: 'inline-flex', alignItems: 'center', gap: '8px',
                      background: '#ecfdf5', border: '1px solid #a7f3d0',
                      padding: '6px 14px', borderRadius: '8px', color: '#047857', fontSize: '13px', fontWeight: '600'
                    }}>
                      <FileCheck size={16} /> {fileName}
                    </div>
                  )}
                </div>
              </div>
            )}

            {/* TAB CONTENT: PASTE TEXT */}
            {activeTab === 'text' && (
              <div>
                <textarea 
                  rows={12}
                  value={contractText}
                  onChange={(e) => setContractText(e.target.value)}
                  placeholder="Dán toàn bộ nội dung hợp đồng vào đây (Bao gồm Tên hợp đồng, Các bên, Điều 1, Điều 2, Điều 3...)..."
                  style={{
                    width: '100%',
                    background: '#f8fafc',
                    border: '1px solid #cbd5e1',
                    borderRadius: '12px',
                    padding: '16px',
                    color: '#0f172a',
                    fontSize: '14px',
                    fontFamily: 'var(--font-mono)',
                    lineHeight: '1.6',
                    resize: 'vertical',
                    outline: 'none'
                  }}
                />
              </div>
            )}

            {/* ERROR ALERT */}
            {errorMsg && (
              <div style={{
                marginTop: '20px', padding: '14px 18px', borderRadius: '10px',
                background: '#fff1f2', border: '1px solid #fecdd3',
                color: '#be123c', fontSize: '13px', display: 'flex', alignItems: 'flex-start', gap: '12px',
                whiteSpace: 'pre-line'
              }}>
                <AlertTriangle size={20} color="#e11d48" style={{ flexShrink: 0, marginTop: '2px' }} />
                <div>{errorMsg}</div>
              </div>
            )}

            {/* ACTION SUBMIT BUTTON */}
            <div style={{ marginTop: '24px', display: 'flex', justifyContent: 'flex-end' }}>
              <button 
                onClick={handleSubmit} 
                className="glow-btn"
                disabled={!contractText.trim()}
              >
                <Zap size={18} /> Phân tích & Xuất Báo cáo Word <ArrowRight size={18} />
              </button>
            </div>

          </div>
        )}

        {/* LOADING & PROGRESS STEP VIEW */}
        {isLoading && (
          <div className="glass-card" style={{ padding: '36px', textAlign: 'center' }}>
            <div style={{ margin: '0 auto 24px auto', position: 'relative', width: '80px', height: '80px' }}>
              <div className="spinning" style={{
                width: '80px', height: '80px', borderRadius: '50%',
                border: '4px solid #e2e8f0',
                borderTopColor: '#0284c7'
              }} />
              <div style={{
                position: 'absolute', top: '50%', left: '50%', transform: 'translate(-50%, -50%)'
              }}>
                <Cpu size={32} color="#0284c7" />
              </div>
            </div>

            <h2 style={{ fontSize: '20px', fontWeight: '700', color: '#0f172a', marginBottom: '8px' }}>
              Đang rà soát Hợp đồng qua n8n AI Pipeline...
            </h2>
            <p style={{ color: '#64748b', fontSize: '14px', marginBottom: '32px' }}>
              Hệ thống đang tiến hành khử trùng dữ liệu, gọi Gemini AI và dựng báo cáo Word chuẩn Nghị định 30
            </p>

            {/* STEPS LIST */}
            <div style={{ maxWidth: '600px', margin: '0 auto', textAlign: 'left', display: 'flex', flexDirection: 'column', gap: '14px' }}>
              {processingSteps.map((step, idx) => {
                const isDone = idx < currentStep;
                const isCurrent = idx === currentStep;
                return (
                  <div 
                    key={idx} 
                    style={{
                      display: 'flex', alignItems: 'center', gap: '14px',
                      padding: '12px 16px', borderRadius: '10px',
                      background: isCurrent ? '#f0f9ff' : isDone ? '#f0fdf4' : '#f8fafc',
                      border: `1px solid ${isCurrent ? '#bae6fd' : isDone ? '#bbf7d0' : '#e2e8f0'}`,
                      transition: 'all 0.3s ease'
                    }}
                  >
                    <div style={{
                      width: '28px', height: '28px', borderRadius: '50%',
                      display: 'flex', alignItems: 'center', justifyContent: 'center',
                      fontSize: '12px', fontWeight: '700',
                      background: isDone ? '#10b981' : isCurrent ? '#0284c7' : '#cbd5e1',
                      color: '#ffffff'
                    }}>
                      {isDone ? <CheckCircle2 size={16} color="#fff" /> : idx + 1}
                    </div>
                    <div>
                      <div style={{ fontSize: '14px', fontWeight: isCurrent || isDone ? '600' : '500', color: isCurrent ? '#0284c7' : isDone ? '#047857' : '#64748b' }}>
                        {step.title}
                      </div>
                      <div style={{ fontSize: '12px', color: '#94a3b8' }}>
                        {step.desc}
                      </div>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        )}

        {/* SUCCESS RESULT & DOWNLOAD VIEW */}
        {downloadBlobUrl && !isLoading && (
          <div className="glass-card" style={{ padding: '36px', textAlign: 'center' }}>
            <div style={{
              width: '72px', height: '72px', borderRadius: '50%',
              background: '#ecfdf5', border: '2px solid #10b981',
              display: 'flex', alignItems: 'center', justifyContent: 'center',
              margin: '0 auto 20px auto', boxShadow: '0 4px 20px rgba(16, 185, 129, 0.25)'
            }}>
              <FileCheck size={36} color="#10b981" />
            </div>

            <h2 style={{ fontSize: '22px', fontWeight: '800', color: '#0f172a', marginBottom: '8px' }}>
              Rà soát Thành công & Đã tạo Báo cáo Word!
            </h2>
            <p style={{ color: '#64748b', fontSize: '14px', marginBottom: '28px' }}>
              File báo cáo <strong>report.docx</strong> đã được tự động tải xuống máy của bạn.
            </p>

            {/* FILE INFO CARD */}
            <div style={{
              maxWidth: '480px', margin: '0 auto 32px auto', padding: '18px 24px',
              background: '#f8fafc', border: '1px solid #e2e8f0',
              borderRadius: '12px', display: 'flex', alignItems: 'center', justifyContent: 'space-between'
            }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '14px', textAlign: 'left' }}>
                <FileCode2 size={32} color="#0284c7" />
                <div>
                  <div style={{ fontSize: '14px', fontWeight: '600', color: '#0f172a' }}>
                    {downloadFileName}
                  </div>
                  <div style={{ fontSize: '12px', color: '#64748b' }}>
                    Kích thước: {(fileSize / 1024).toFixed(1)} KB • Định dạng Word (.docx)
                  </div>
                </div>
              </div>
            </div>

            {/* ACTION BUTTONS */}
            <div style={{ display: 'flex', justifyContent: 'center', gap: '16px', flexWrap: 'wrap' }}>
              <a 
                href={downloadBlobUrl} 
                download={downloadFileName} 
                className="glow-btn"
                style={{ textDecoration: 'none' }}
              >
                <Download size={18} /> Tải lại file Báo cáo Word (.docx)
              </a>

              <button 
                onClick={() => {
                  setDownloadBlobUrl(null);
                  setContractText('');
                  setFileName('');
                }}
                className="secondary-btn"
                style={{ padding: '12px 20px' }}
              >
                <RefreshCw size={16} /> Rà soát Hợp đồng khác
              </button>
            </div>
          </div>
        )}

      </div>
    </div>
  );
}
