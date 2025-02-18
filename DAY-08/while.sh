while kubectl get deployment/myapp | grep -q 0/1; do
    echo "Waiting for myapp to be ready..."
    sleep 10
done

while ! aws ec2 describe-instance-status --instance-ids i-1234567890abcdef0 | grep -q "running"; do
    echo "Waiting for the EC2 instance to be running..."
    sleep 10
done

while true; do
    if tail -n 1 /var/log/app.log | grep -q "ERROR"; then
        send_alert "Error detected in the log."
    fi
    sleep 5
done

while true; do
    if ! check_service_health; then
        restart_service
    fi
    sleep 30
done