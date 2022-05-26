def findDecision(obj):
   # Feature: RSI, Instances: 115, Entropy: 0.9802
   if obj[1] == 'Hold':
      # Feature: SMA1, Instances: 94, Entropy: 0.9948
      if obj[4] == 'Buy':
         # Feature: SMA2, Instances: 52, Entropy: 0.9118
         if obj[5] == 'Buy':
            # Feature: BB, Instances: 40, Entropy: 0.7692
            if obj[3] == 'Sell':
               # Feature: MACD, Instances: 24, Entropy: 0.9183
               if obj[2] == 'Sell':
                  # Feature: Closing, Instances: 23, Entropy: 0.9321
                  if obj[0]>4.944:
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[2] == 'Buy':
                  return 'Yes'
               else:
                  return 'Yes'
            elif obj[3] == 'Hold':
               # Feature: MACD, Instances: 16, Entropy: 0.3373
               if obj[2] == 'Buy':
                  # Feature: Closing, Instances: 11, Entropy: 0.4395
                  if obj[0]>4.944:
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[2] == 'Sell':
                  return 'Yes'
               else:
                  return 'Yes'
            else:
               return 'Yes'
         elif obj[5] == 'Sell':
            # Feature: MACD, Instances: 12, Entropy: 0.9183
            if obj[2] == 'Sell':
               # Feature: Closing, Instances: 6, Entropy: 0.65
               if obj[0]>4.944:
                  # Feature: BB, Instances: 6, Entropy: 0.65
                  if obj[3] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[2] == 'Buy':
               # Feature: BB, Instances: 6, Entropy: 1.0
               if obj[3] == 'Sell':
                  # Feature: Closing, Instances: 5, Entropy: 0.971
                  if obj[0]>4.944:
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[3] == 'Hold':
                  return 'No'
               else:
                  return 'No'
            else:
               return 'No'
         else:
            return 'No'
      elif obj[4] == 'Sell':
         # Feature: Closing, Instances: 42, Entropy: 0.9587
         if obj[0]>4.944:
            # Feature: SMA2, Instances: 39, Entropy: 0.9766
            if obj[5] == 'Sell':
               # Feature: BB, Instances: 23, Entropy: 0.9986
               if obj[3] == 'Sell':
                  # Feature: MACD, Instances: 17, Entropy: 0.9774
                  if obj[2] == 'Buy':
                     return 'No'
                  elif obj[2] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               elif obj[3] == 'Buy':
                  # Feature: MACD, Instances: 4, Entropy: 1.0
                  if obj[2] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               elif obj[3] == 'Hold':
                  return 'Yes'
               else:
                  return 'Yes'
            elif obj[5] == 'Buy':
               # Feature: MACD, Instances: 16, Entropy: 0.896
               if obj[2] == 'Buy':
                  # Feature: BB, Instances: 11, Entropy: 0.9457
                  if obj[3] == 'Hold':
                     return 'No'
                  elif obj[3] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               elif obj[2] == 'Sell':
                  # Feature: BB, Instances: 5, Entropy: 0.7219
                  if obj[3] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            else:
               return 'No'
         elif obj[0]<=4.944:
            return 'No'
         else:
            return 'No'
      else:
         return 'No'
   elif obj[1] == 'Sell':
      # Feature: SMA1, Instances: 17, Entropy: 0.3228
      if obj[4] == 'Buy':
         return 'Yes'
      elif obj[4] == 'Sell':
         # Feature: Closing, Instances: 4, Entropy: 0.8113
         if obj[0]>4.944:
            # Feature: MACD, Instances: 4, Entropy: 0.8113
            if obj[2] == 'Buy':
               # Feature: BB, Instances: 4, Entropy: 0.8113
               if obj[3] == 'Hold':
                  # Feature: SMA2, Instances: 4, Entropy: 0.8113
                  if obj[5] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            else:
               return 'Yes'
         else:
            return 'Yes'
      else:
         return 'Yes'
   elif obj[1] == 'Buy':
      return 'No'
   else:
      return 'No'
