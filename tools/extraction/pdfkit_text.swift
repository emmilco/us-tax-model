import Foundation
import PDFKit
let args = CommandLine.arguments
let doc = PDFDocument(url: URL(fileURLWithPath: args[1]))!
let first = args.count > 2 ? Int(args[2])! : 1
let last = args.count > 3 ? Int(args[3])! : doc.pageCount
for p in first...last {
    if let page = doc.page(at: p - 1) { print(page.string ?? "") }
    print("\u{0C}", terminator: "")
}
